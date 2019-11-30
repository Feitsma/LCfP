"Exercise 11.1.12"

import math

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
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,4)
r = p.halfway(q)
print(r)

