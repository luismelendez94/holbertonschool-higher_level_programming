#!/usr/bin/python3


def search_replace(my_list, search, replace):

    new_list = my_list.copy()
    index = 0
    for element in my_list:
        index += 1
        if element == search:
            new_list[index] = replace

    return new_list
