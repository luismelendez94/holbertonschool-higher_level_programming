#!/usr/bin/python3
""" The class Rectangle inherit class geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherit from BaseGeometry """

    def __init__(self, width, height):
        """ Initialize private variables """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Compute the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the rectangle """

        return "[Rectangle] " + str(self.__width) + "/\
" + str(self.__height)
