#!/usr/python3
""" Lets read a text file """


def read_file(filename=""):
    """ Reads a text file and prints it out """

    with open(filename, 'r') as readFile:
        fileData = readFile.read()
    for line in fileData:
        print(line, end='')
    readFile.closed
