#!/usr/bin/python3
"""This is the class Rectangle"""


class Rectangle:
    """An example of an empty class"""

    def __init__(self, width=0, height=0):
        """Optional initialize of variables width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: Set and verify the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: Set and verify the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
