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
