#!/usr/bin/python3
"""This is the class Square"""


class Square:
    """Compute the area of the square"""

    def __init__(self, size=0):
        """Initialize variable size"""

        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """Compute the area size of a square"""

        return self.__size ** 2
