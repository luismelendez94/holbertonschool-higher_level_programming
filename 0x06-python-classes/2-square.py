#!/usr/bin/python3
"""This is the class Square"""


class Square:
    """Size validation of the square"""

    def __init__(self, size=0):
        """Initialize variable size Verify that it is a integer"""

        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
