#!/usr/bin/python3
""" This is the class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square inherits from the class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialice all variables pass """

        super().__init__(size, size, x, y, id)

    def area(self):
        """ Compute the area of a rectangle """

        return self.__width * self.__height

    def display(self):
        """ Print a rectangle with the specifications """

        for line in range(self.__y):
            print()
        for col in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            if col < self.__height - 1:
                print()
        print()

    def __str__(self):
        """ Return a string representation of the rectangle """

        return "[Square] " + "(" + str(self.id) + ") " + str(self.__x) + "/\
" + str(self.__y) + " - " + str(self.__size)

"""
def update(self, *args, **kwargs):
        Assigns an argument to each attribute

        if args is None:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.__width = value
                if key == 2:
                    self.__height = value
                if key == 3:
                    self.__x = value
                if key == 4:
                    self.__y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y
"""
