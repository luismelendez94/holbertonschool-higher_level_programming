#!/usr/bin/python3
"""This is the class Rectangle"""


class Rectangle:
    """Defining class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Optional initialize of variables width and height"""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: Set and verify the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: Set and verify the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string with the rectangle"""

        retString = ""
        if self.__width == 0 or self.__height == 0:
            return retString
        else:
            for col in range(self.__height):
                for row in range(self.__width):
                    retString += str(self.print_symbol)
                if col < self.__height - 1:
                    retString += "\n"
            return retString

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return "Rectangle(" + str(self.__width) + ", \
" + str(self.__height) + ")"

    def __del__(self):
        """Delete a rectangle"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and returns the biggest"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if (area1 == area2) or (area1 > area2):
            return rect_1
        elif (area1 < area2):
            return rect_2

    @classmethod
    def square(cls, size):
        """Create rectangle width == height"""

        return cls(size, size)
