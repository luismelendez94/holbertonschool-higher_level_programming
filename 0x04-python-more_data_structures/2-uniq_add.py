#!/usr/bin/python3


def uniq_add(my_list=[]):

    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    addition = 0
    for element in new_list:
        addition += element
    return addition
