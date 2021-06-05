#!/usr/bin/python3
""" Lets see what is the string of a JSON """


def from_json_string(my_str):
    """ Return the object of an JSON """

    import json

    return(json.loads(my_str))
