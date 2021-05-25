#!/usr/bin/python3
"""This is the class Rectangle"""


class Rectangle:
    """Defining class Rectangle"""

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

    def area(self):
        """Compute the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string with the rectangle"""

        retString = ""
        if self.__width == 0 or self.__height == 0:
            return retString
        else:
            for col in range(self.__height):
                for row in range(self.__width):
                    retString += "#"
                if col < self.__height - 1:
                    retString += "\n"
            return retString

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return "Rectangle(" + str(self.__width) + ", \
" + str(self.__height) + ")"
