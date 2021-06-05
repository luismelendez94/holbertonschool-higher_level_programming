#!/usr/bin/python3
""" The class Square inherit class Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherit from Rectangle """

    def __init__(self, size):
        """ Initialize private variable """

        super().integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Compute the area of a square """
        return self.__size * self.__size
