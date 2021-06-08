#!/usr/bin/python3
""" This is the class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square inherits from the class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialice all variables pass """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter: Retrieve the size """

        return Rectangle.width.fget(self)

    @size.setter
    def size(self, value):
        """ Setter: Set and verify the size """

        Rectangle.width.fset(self, value)

    def __str__(self):
        """ Return a string representation of the rectangle """

        return "[Square] " + "(" + str(self.id) + ") " + str(self.x) + "/\
" + str(self.y) + " - " + str(self.size)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """

        if args and args is not None:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.size = value
                if key == 2:
                    self.x = value
                if key == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return dictionary representation of Square """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
