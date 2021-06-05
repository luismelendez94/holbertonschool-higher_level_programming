#!/usr/bin/python3
""" Lets see what is the JSON of a string """


def to_json_string(my_obj):
    """ Return the json of an object """

    import json

    return(json.dumps(my_obj))
