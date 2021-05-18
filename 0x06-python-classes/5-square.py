#!/usr/bin/python3
"""This is the class Square"""


class Square:
    """Print a square"""

    def __init__(self, size=0):
        """Initialize variable size"""

        self.__size = size

    def area(self):
        """Compute the area size of a square"""

        return self.__size ** 2

    @property
    def size(self):
        """Setter: Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Getter: Set and verify the size"""

        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Print the square"""

        if self.__size != 0:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                if i != self.__size:
                    print()
        else:
            print()
