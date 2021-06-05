#!/usr/bin/python3
""" Lets write at the end of a text file """


def append_write(filename="", text=""):
    """ Write something in the end of a file """

    with open(filename, 'a+') as f:
        f.write(text)

    return(len(text))
