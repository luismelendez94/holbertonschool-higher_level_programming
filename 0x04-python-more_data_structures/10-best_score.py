#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    maxValue = 0
    maxKey = 0
    for key, value in a_dictionary.items():
        if maxValue < value:
            maxValue = value
            maxKey = key
    return maxKey
