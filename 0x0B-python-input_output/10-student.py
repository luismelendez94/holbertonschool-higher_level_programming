#!/usr/bin/python3
""" This is the class Student """


class Student:
    """ Class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize the instances in Student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves the dictionary representation """

        if attrs is not None:
            newList = {}
            for index in attrs:
                if index in self.__dict__:
                    newList[index] = self.__dict__[index]
            return newList

        return(self.__dict__)
