#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    difference = set(set_1).symmetric_difference(set(set_2))
    list_difference = list(difference)

    return list_difference
