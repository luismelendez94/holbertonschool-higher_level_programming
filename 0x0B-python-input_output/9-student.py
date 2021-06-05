#!/usr/bin/python3
""" This is the class Student """


class Student:
    """ Class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize the instances in Student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves the dictionary representation """

        return(self.__dict__)
