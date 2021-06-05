#!/usr/bin/python3
""" Lets write a text file """


def write_file(filename="", text=""):
    """ Write something in to a file """

    with open(filename, 'w+') as f:
        f.write(text)

    return(len(text))
