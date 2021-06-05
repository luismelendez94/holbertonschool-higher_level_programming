#!/usr/bin/python3
""" Lets creates Object from a JSON file """


def load_from_json_file(filename):
    """ Create an Object from a JSON file """

    import json

    with open(filename, 'r') as readFile:
        return(json.load(readFile))
