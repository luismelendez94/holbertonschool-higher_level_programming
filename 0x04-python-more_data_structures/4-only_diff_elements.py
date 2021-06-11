#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    new_list = []
    for element1 in set_1:
        for element2 in set_2:
            if element1 not in set_2 and element1 not in new_list:
                new_list.append(element1)
            elif element2 not in set_1 and element2 not in new_list:
                new_list.append(element2)
    return new_list
