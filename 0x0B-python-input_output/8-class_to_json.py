#!/usr/bin/python3
""" Script to return the dictionary description of a obj """


def class_to_json(obj):
    """ Returns de dictionary description of obj that
    is a instance of a class """

    return obj.__dict__
