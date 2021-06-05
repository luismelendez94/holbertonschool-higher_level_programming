#!/usr/bin/python3
""" Lets write Object to a text file """


def save_to_json_file(my_obj, filename):
    """ Write Object to a file using JSON """

    import json

    with open(filename, 'w+') as writeFile:
        json.dump(my_obj, writeFile)
