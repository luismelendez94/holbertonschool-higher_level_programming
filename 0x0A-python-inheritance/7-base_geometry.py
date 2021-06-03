#!/usr/bin/python3
""" This is the class BaseGeometry """


class BaseGeometry:
    """ An example of an empty class """

    def area(self):
        """ Calculates the area of geometry """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is from name """

        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
