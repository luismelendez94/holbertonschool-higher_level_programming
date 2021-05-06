#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxNumber = -99
    for item in my_list:
        if item > maxNumber:
            maxNumber = item
    return maxNumber
