"Exercise 11.1.12 of How to Think Like a ComputerScientist: Learning with Python 3Documentation"

import math
import datetime
import time

class Point:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """Return the halfway point between myself and target"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        """Reflects a point around x-axis"""
        x = self.x
        y = self.y * -1
        return Point(x, y)

    def slope_from_origin(self):
        origin = Point(0, 0)
        dx = self.x - origin.x
        dy = self.y - origin.y
        return (dy / dx)

    def get_line_to(self, target):
        """determine a and b in y=ax+b"""
        # a is slope of line
        # b is distance in x value
        dx = target.x - self.x
        dy = target.y - self.y
        return Point(dy / dx, dy)


# print(Point(4,11).get_line_to(Point(6,15)))