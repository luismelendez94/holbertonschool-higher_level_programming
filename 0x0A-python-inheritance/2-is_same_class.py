#!/usr/bin/python3
""" Lets verify if object is of the specified class or not """


def is_same_class(obj, a_class):
    """ Verify if the object its from class """

    if (type(obj) == a_class):
        return True
    return False
