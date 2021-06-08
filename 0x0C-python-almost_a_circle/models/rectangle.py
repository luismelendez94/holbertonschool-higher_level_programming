#!/usr/bin/python3
""" This is the class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ The class Rectangle inherits from the class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialice all variables pass """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter: Retrieve the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter: Set and verify the width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Getter: Retrieve the height """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter: Set and verify the height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Getter: Retrieve the x value """

        return self.__x

    @x.setter
    def x(self, value):
        """ Setter: Set and verify the x value """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Getter: Retrieve the y value """

        return self.__y

    @y.setter
    def y(self, value):
        """ Setter: Set and verify the y value """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

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

        return "[Rectangle] " + "(" + str(self.id) + ") " + str(self.__x) + "/\
" + str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """

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
