#!/usr/bin/python3
""" Lets create the class Base,
    this class its to manage id attribute in all future classes
    and to avoid duplicating the same code """


class Base():
    """ This class will be the base of all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialice the id """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
