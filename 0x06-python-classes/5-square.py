#!/usr/bin/python3
"""introducing my_print(self)"""


class Square:
    """def my_print(self)"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return size.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if self.__size == 0:
            print()

        for j in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
