#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elems = 0
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            elems += 1
    except:
        pass
    print("")
    return (elems)
