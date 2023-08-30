#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Coordinates of a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(sef, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        s = self.__size

        if s == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(s):
                print(" " * self.__position[0], end="")
                for j in range(s):
                    print("#", end="")
                print()
