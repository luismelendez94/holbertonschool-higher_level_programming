#!/usr/bin/python3
""" Lets create the class Base,
    this class its to manage id attribute in all future classes
    and to avoid duplicating the same code """

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation """

        returnList = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for obj in list_objs:
                returnList.append(cls.to_dictionary(obj))
        with open(filename, 'w') as writeFile:
            writeFile.write(cls.to_json_string(returnList))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """

        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """

        filename = cls.__name__ + ".json"
        returnList = []

        try:
            with open(filename, 'r') as jsonFile:
                returnList = cls.from_json_string(jsonFile.read())
            for key, value in enumerate(returnList):
                returnList[key] = cls.create(**returnList[key])
        except:
            pass
        return returnList
