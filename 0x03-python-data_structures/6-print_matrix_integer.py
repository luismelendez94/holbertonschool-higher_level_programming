#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for column in row:
            count = count + 1
            print("{:d}".format(column), end="")
            if count < len(matrix[count - 1]):
                print(" ", end="")
        print()
