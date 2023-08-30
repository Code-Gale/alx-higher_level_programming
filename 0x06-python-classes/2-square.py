#!/usr/bin/python3
"""Creating class Square with Instantiation"""


class Square:
    """introducing instatiation"""
    def __init(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
