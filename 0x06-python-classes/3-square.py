#!/usr/bin/python3
"""Getting area of square"""


class Square:
    """getting area of the square based on 2-square.py"""
    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return int(self.__size) * int(self.__size)
