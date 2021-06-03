#!/usr/bin/python3
""" Lets verify if object is an instance of, or if the object
    is an instance of a class that inherited from, the class """


def is_kind_of_class(obj, a_class):
    """ Verify if obj is from class or
        if obj is from an instance of class """

    if isinstance(obj, a_class):
        return True
    return False
