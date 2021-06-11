#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    dict_items = sorted(a_dictionary.items())

    for key, value in dict_items:
        print("{}: {}".format(key, value))
