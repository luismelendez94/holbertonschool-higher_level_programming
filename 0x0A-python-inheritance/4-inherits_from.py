#!/usr/bin/python3
""" Lets verify if object is an instance of a class that
    inherited (directly or indirectly) from specified class """


def inherits_from(obj, a_class):
    """ Verify if obj is from class """

    if issubclass(type(obj), a_class):
        return True
    return False
